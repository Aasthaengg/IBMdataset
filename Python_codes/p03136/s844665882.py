n = int(input())
l = list( map(int,input().split()) )

a = max(l)
b = sum(l) - a

print('Yes' if a < b else 'No')