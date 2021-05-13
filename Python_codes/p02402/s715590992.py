list = []
n = input()
list = map(int,raw_input().split())

print '%d %d %d' % (min(list),max(list),sum(list))