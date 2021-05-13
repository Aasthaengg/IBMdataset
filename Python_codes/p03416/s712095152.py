def resolve():
    '''
    code here
    '''
    A, B = [int(item) for item in input().split()]

    res = 0
    for i in range(A, B+1):
        temp_num_str = str(i)
        for j in range(len(temp_num_str)//2):
            if temp_num_str[j] != temp_num_str[-1 * (j+1)]:
                break
        else:
            res += 1

    print(res)
if __name__ == "__main__":
    resolve()
