k = int(input())

digit_len = 1

def df(num, depth):
    if len(str(num)) == depth:
        return [num]

    df_result = []
    tmp_num = int(str(num)[-1])
    tmp = [tmp_num]
    if tmp_num-1>=0:
        tmp.append(tmp_num-1)
    if tmp_num+1<10:
        tmp.append(tmp_num+1)
    for i in tmp:
        df_result.extend(df(int(str(num)+str(i)), depth))
    return df_result

num_list = []
while 1:
    tmp = []
    for i in range(1,10):
        tmp.extend(df(i, digit_len))
    num_list.extend(sorted(tmp))
    if len(num_list)>=k:
        break
    digit_len+=1

print(num_list[k-1])
