a, b, c, d = map(int, input().split())
takahashi = (a+d-1)//d
aoki = (c+b-1)//b

print('Yes') if takahashi >= aoki else print('No')