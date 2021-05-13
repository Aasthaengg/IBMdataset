import collections
 
 
class Node(object):
 
  def __init__(self):
    self.value = 0
    self.edges = [] 
 
def main():
  n = int(input())
  nodes = [Node() for _ in range(n)]
 
  for _ in range(n - 1):
    a, b = map(int, input().split())
    nodes[a - 1].edges.append(nodes[b - 1])
    nodes[b - 1].edges.append(nodes[a - 1])
 
  values = list(map(int, input().split()))
  values.sort(reverse=True)
 
  print(sum(values[1:]))
 
  queue = collections.deque()
  queue.append(nodes[0])
  index = 0
 
  while len(queue) != 0:
    node = queue.popleft()
    node.value = values[index]
    index += 1
 
    queue.extend(n for n in node.edges if n.value == 0)
 
  print(' '.join(str(n.value) for n in nodes))
 
 
if __name__ == '__main__':
  main()
 