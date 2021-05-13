n = int(input())
l = list(map(int, input().split()))

l_s = list(sorted(l))
print( 'Yes' if (l_s[-1] < sum(l_s[:-1])) else 'No')