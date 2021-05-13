input_num = str(input())
cnt_2_in_str = lambda x: 1 if x == '2' else 0
print(sum(map(cnt_2_in_str,input_num)))
