import copy
def magic(arr,i,k):
  if(k==0):
    if(arr[0] < arr[1] and arr[1] < arr[2]):
      return True
    else:
      return False
  k-=1
  arr[i]*=2
  return magic(arr.copy(),0,k) or magic(arr.copy(),1,k) or magic(arr.copy(),2,k)
  
if __name__ == "__main__":
  arr = list(map(int,input().split()))
  k = int(input())
  if(magic(arr.copy(),0,k) or magic(arr.copy(),1,k) or magic(arr.copy(),2,k)):
    print("Yes")
    exit()
  else:
    print("No")