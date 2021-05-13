s = str(input().split())
i = 0 + 2
while True:
    if s[i] == s[i + 1]:
        print_ans = 'Bad'
        break
    else:
        print_ans = 'Good'
    i += 1
    if i == 3 + 2:
        break
    
print(print_ans)