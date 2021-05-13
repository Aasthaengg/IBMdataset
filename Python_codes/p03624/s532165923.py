s_list = list(input())

result = None

for s_uni in range(ord('a'), ord('z') + 1):
    if not chr(s_uni) in s_list:
        result = chr(s_uni)
        break

if result:
    print(result)
else:
    print('None')
