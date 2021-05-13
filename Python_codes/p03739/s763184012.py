from sys import stdin


if __name__ == "__main__":
    _in = [_.rstrip() for _ in stdin.readlines()]
    n = int(_in[0])  # type:int
    a_arr = list(map(int,_in[1].split(' ')))  # type:list(int)
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    cnt0 = 0
    sum_ = 0
    for i in range(0,n):
        if i%2 == 0:
            if sum_+a_arr[i]<=0:
                cnt0 += 1-(sum_+a_arr[i])
                sum_ = 1
            else:
                sum_ = sum_+a_arr[i]
        else:
            if sum_+a_arr[i]>=0:
                cnt0 += 1+(sum_+a_arr[i])
                sum_ = -1
            else:
                sum_ = sum_+a_arr[i]
    cnt1 = 0
    sum_ = 0
    for i in range(0,n):
        if i%2 == 1:
            if sum_+a_arr[i]<=0:
                cnt1 += 1-(sum_+a_arr[i])
                sum_ = 1
            else:
                sum_ = sum_+a_arr[i]
        else:
            if sum_+a_arr[i]>=0:
                cnt1 += 1+(sum_+a_arr[i])
                sum_ = -1
            else:
                sum_ = sum_+a_arr[i]
    cnt = min(cnt0,cnt1)
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(cnt)
