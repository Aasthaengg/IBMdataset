# solution
import io

nim,mike = map(int,input().split())
array = list(map(int,input().split()))
arrays = []
min_a = float("inf")
for a in array:
   min_a = min(a, min_a)
   arrays.append(min_a)
array2 = []
for a,b in zip(array, arrays):
   array2.append(a-b)
array2 = sorted(array2)
print(array2.count(array2[-1]))