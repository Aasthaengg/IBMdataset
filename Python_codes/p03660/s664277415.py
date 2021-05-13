import typing
from typing import List, NamedTuple, Deque, Set, Counter

class node:
    def __init__(self, id: int) -> None:
        self.id: int = id
        self.parent: node = self
        self.root: node = self
        self.rank: int = 0
        self.connection: List[node] = []

    def addConnection(self, other: 'node') -> None:
        self.connection.append(other)
        other.connection.append(self)

    def delConnection(self, other: 'node') -> None:
        self.connection.remove(other)
        other.connection.remove(self)

    def setParent(self, other: 'node') -> None:
        self.parent = other
        self.rank = other.rank +1
    
    def setRoot(self, other: 'node') -> None:
        self.root = other

    def setAsRoot(self) -> None:
        self.parent = self
        self.root = self
        self.rank = 0


def makePath(root: node, target: node) -> Deque[node]:
    path: Deque[node] = Deque()
    path.append(target)
    while path[0] != root:
        path.appendleft(path[0].parent)
    return path


def bfs(root: node):
    reserved: Deque[node] = Deque([root])
    seen: Set[int] = {root.id}
    while len(reserved) > 0:
        current_node = reserved.popleft()
        for next_node in current_node.connection:
            if next_node.id in seen:
                continue
            next_node.setParent(current_node)
            next_node.setRoot(root)
            seen.add(next_node.id)
            reserved.append(next_node)


def main():
    N = int(input())
    Edge = [map(int, input().split()) for _ in range(N-1)]

    Node: List[node] = [node(i) for i in range(N)]
    for a, b in Edge:
        Node[a-1].addConnection(Node[b-1])

    #Node[0]からbfs
    bfs(Node[0])
    #between:Node[0]とNode[N-1]の間にあるノード数
    between: int = Node[N-1].rank -1
    #sep:お互い陣地を取り合った時に衝突する点までの距離fromNode[0]
    sep = (between+1)//2
    path = makePath(Node[0], Node[N-1])
    #衝突点の結合を削除, 再度bfs
    path[sep].delConnection(path[sep+1])
    path[sep+1].setAsRoot()
    bfs(path[sep+1])
    #2分した木のノード数集計
    fennec, snuke = Counter([n.root.id for n in Node]).values()
    #勝者判定
    print('Fennec' if fennec > snuke else 'Snuke')


if __name__ == '__main__':
    main()