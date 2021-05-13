def cal(S):
    N = len(S)
    num,cnt = 0,0
    mod = 2019
    rem_dict,rem_set = {},set()
    for i in range(N):
        num = (num + int(S[N-1-i]) * pow(10,i,mod)) % mod
        if num in rem_set:
            rem_dict[num] += 1
        else:
            rem_set.add(num)
            rem_dict[num] = 1

    if 0 in rem_set:
        output = rem_dict[0] * (rem_dict[0] + 1) // 2
    else:
        output = 0
    rem_set.discard(0)
    for rem in rem_set:
        output += rem_dict[rem] * (rem_dict[rem]-1) // 2

    return output

def main():
    S = input()

    print(cal(S))

if __name__ == "__main__":
    main()
