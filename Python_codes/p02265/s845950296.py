from collections import deque

lst = deque()

for l in range(int(input())):
  dat_set = input().split()
  command = dat_set[0]
  try:
    if command == 'insert':
      lst.appendleft(dat_set[-1])
    elif command == 'delete':
      lst.remove(dat_set[-1])
    elif command == 'deleteFirst':
      lst.popleft()
    elif command == 'deleteLast':
      lst.pop()
  except:
    pass

print(*lst)
