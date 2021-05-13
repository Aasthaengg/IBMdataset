N = list(map(int,input().split()))
N.sort()
print("YES" if N[0]*1000+N[1]*100+N[2]*10+N[3] == 1479 else "NO")
