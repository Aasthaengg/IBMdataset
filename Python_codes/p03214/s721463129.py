n = int(input())
li = list(map(int,input().split()))

x = sum(li)/n
li = [abs(i-x) for i in li]

print(li.index(min(li)))
