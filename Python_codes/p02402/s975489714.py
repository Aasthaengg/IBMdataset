num = int( input() )
ls = list(map(int, input().split() ) )

print(min(ls), end=" ")
print(max(ls), end=" ")
print(sum(ls))