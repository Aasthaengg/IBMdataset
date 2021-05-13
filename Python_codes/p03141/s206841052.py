N=int(input())
AB=[tuple(map(int, input().split()))for _ in range(N)]
AB.sort(key=lambda ab: ab[0]+ab[1], reverse=True)
print(sum(a for a,b in AB[0::2])-sum(b for a,b in AB[1::2]))