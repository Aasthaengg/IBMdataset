n = int(input())
a_list = [int(input()) for _ in range(n)]

is_odd = [x%2==0 for x in a_list]

if all(is_odd):
    print('second')
else:
    print('first')