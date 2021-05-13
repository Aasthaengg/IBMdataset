MM = input().split()
N =int(MM[0])
M =int(MM[1])
list1 = [i for i in range(M+1)]
for i in range(N):
  MM = input().split()
  list2 = [int(MM[j]) for j in range(1,int(MM[0])+1)]
  list1 = set(list1)&set(list2)
print(len(list1))
