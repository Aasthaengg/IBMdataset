n = int(input())
min_ = 0
list_ = set(list(map(int, input().split())))

while True:
  tmp = min(list_)
  list_ = set([i%tmp for i in list_])
  if 0 in list_:
    list_.remove(0)
  list_.add(tmp)
  if tmp==min(list_):
    break
print(tmp)