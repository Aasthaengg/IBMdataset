n,k = map(int,input().split())
a_list = list(map(int,input().split()))
how = [0]*n
for a in a_list:
  how[a-1] += 1
how.sort(reverse=True)
total = sum(how[:k])
print(n-total)