A, B = map(int, input().split())

ans_list = [x for x in range(A, B+1) if list(str(x)) == list(reversed(str(x)))]
print(len(ans_list))