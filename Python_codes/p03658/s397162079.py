x, y = map(int,input().split())
li = list(map(int,input().split()))
li.sort(reverse=True)

print(sum(li[:y]))