a, b, c = map(int, input().split())
list_abc = [a, b, c]
list_abc.sort(reverse=True)
ans = int(str(list_abc[0]) + str(list_abc[1])) + list_abc[2]
print(ans)