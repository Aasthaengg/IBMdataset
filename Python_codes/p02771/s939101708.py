def poor():
    # 入力
    num_set = set(map(int, input().split()))
    # 処理
    if len(num_set) == 2:
        return 'Yes'
    else:
        return 'No'

result = poor()
print(result)