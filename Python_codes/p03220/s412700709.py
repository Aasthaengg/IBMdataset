n = int(input())
t, a = map(int, input().split())
listh = list(map(int, input().split()))
diff = [abs((t-x*0.006)-a) for x in listh]
print(diff.index(min(diff))+1)
