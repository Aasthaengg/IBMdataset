

a,b = map(int,input().split())

a_list = [i for i in range(1,a+1)]
b_list = [i for i in range(1,b+1)]


a_len = len(a_list)
b_len = len(b_list)


if a_len < b_len:
    print(a_len)
elif a_len == b_len:
    print(a_len)
elif a_len>b_len:
    ans = a_len-1
    print(ans)