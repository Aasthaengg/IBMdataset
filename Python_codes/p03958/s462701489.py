k,t = map(int,input().split())
ai = [int(i) for i in input().split()]

ai.sort(reverse=True)

print(max(0,ai[0]-(sum(ai)-ai[0])-1))