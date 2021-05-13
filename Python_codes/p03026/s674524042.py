from collections import deque

class Node:
    def __init__(self):
        self.val = -1
        self.link = []

def main():
    N = int(input())
    nodes = [Node() for i in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        a -= 1; b -= 1;
        nodes[a].link.append(nodes[b])
        nodes[b].link.append(nodes[a])
    c = list(map(int, input().split()))
    c = sorted(c, reverse=True)
    count = 0
    q = deque()
    q.append(nodes[0])
    while len(q) > 0:
        node = q.popleft()
        node.val = c[count]
        count += 1
        for next in node.link:
            if next.val == -1:
                q.append(next)
    print(sum(c) - c[0])
    for i in range(N):
        print(nodes[i].val, end="")
        if i != N-1:
            print(" ",end="")
        else:
            print()

if __name__ == "__main__":
    main()
