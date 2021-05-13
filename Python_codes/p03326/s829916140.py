N,M = map(int,input().split())
arr1 = []
arr2 = []
arr3 = []
arr4 = []
arr5 = []
arr6 = []
arr7 = []
arr8 = []

for i in range(N):
  a,b,c = map(int,input().split())
  arr1.append(int(a+b+c))
  arr2.append(int(a-b+c))
  arr3.append(int(a+b-c))
  arr4.append(int(a-b-c))
  arr5.append(int(-a+b+c))
  arr6.append(int(-a-b+c))
  arr7.append(int(-a+b-c))
  arr8.append(int(-a-b-c))

arr1.sort(reverse=True)
arr2.sort(reverse=True)
arr3.sort(reverse=True)
arr4.sort(reverse=True)
arr5.sort(reverse=True)
arr6.sort(reverse=True)
arr7.sort(reverse=True)
arr8.sort(reverse=True)

print(max(sum(arr1[:M]),sum(arr2[:M]),sum(arr3[:M]),sum(arr4[:M]),sum(arr5[:M]),sum(arr6[:M]),sum(arr7[:M]),sum(arr8[:M])))
