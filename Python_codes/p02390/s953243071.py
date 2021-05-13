s = int(input())


base = s // 60

print('{}:{}:{}'.format(base // 60, base%60, s%60))