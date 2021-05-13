a,b,c = map(int,input().split())

lists = [a,b,c]

maxi = max(lists)
mini = min(lists)

print(maxi*10 + a + b + c -maxi)