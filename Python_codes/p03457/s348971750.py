n = int(input())

st_t = 0
st_x = 0
st_y = 0
li_in = list()
for i in range(n):
    li_in.append(list(map(int, input().split())))


for t, x, y in li_in:
    time = t - st_t
    diff_x = abs(x - st_x)
    diff_y = abs(y - st_y)

    if diff_x + diff_y > time:
        print('No')
        exit(0)
    elif diff_x + diff_y == time:
        st_t = t
        st_x = x
        st_y = y
        continue
    # elif diff_x + diff_y < t:
    else:
        if (time - (diff_x + diff_y)) % 2 == 0:
            st_t = t
            st_x = x
            st_y = y
            continue
        else:
            print('No')
            exit(0)
else:
    print('Yes')
