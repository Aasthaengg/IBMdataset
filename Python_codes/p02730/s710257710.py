S = list(input())
l = len(S)

def judge(arr):
  l = len(arr)
  if len(arr) % 2 != 0:
    l = len(arr)
  for i in range(int(l/2)):
    if arr[i] != arr[l-1-i]:
      print("No")
      exit()
      
judge(S)
center = int((l-1)/2)
judge(S[0:center])
judge(S[center+1:])
print("Yes")