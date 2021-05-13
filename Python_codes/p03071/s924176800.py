ab = list(map(int,input().split()))
ab2 = sorted(ab)
coin = ab2[1]
ab2[1] = ab2[1]-1
ab3 = sorted(ab2)
coin += ab3[1]
print(coin)