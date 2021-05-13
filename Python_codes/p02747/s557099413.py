S = input()
hitachi_str = ['hi']
for i in range(0, 10):
  hitachi_str.append(hitachi_str[i] + 'hi')
print('Yes' if S in hitachi_str else 'No')