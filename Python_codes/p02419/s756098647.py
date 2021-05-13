key = input()
count = 0

while True:
    l = list(map(str, input().split()))
    l_lower = [ s.lower() for s in l]
    count += l_lower.count(key)
    if l[-1] == 'END_OF_TEXT':
        break

print(count)