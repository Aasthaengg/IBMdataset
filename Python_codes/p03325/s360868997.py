n = int(input())
aaa = list(map(lambda x: format(int(x), 'b')[::-1].find('1'), input().split()))
print(sum(aaa))