def solve():
    n,m,k = list(map(int,input().split()))
    arr = list(map(int, input().split()))
    arr1 = list(map(int, input().split()))
    aTrack = 0
    bTrack = sum(arr1)
    Bn = len(arr1)
    ans = 0
    for An in range(len(arr)+1):
      if An>0:
        aTrack += arr[An-1]
      if aTrack>k:
        break
      while aTrack+bTrack>k:
        Bn -= 1
        bTrack -= arr1[Bn]
      ans = max(ans, An+Bn)
    print(ans)
    
            
solve()