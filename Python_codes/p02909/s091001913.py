S = input()

if S == 'Sunny':
    answer = 'Cloudy'
elif S == 'Cloudy':
    answer = 'Rainy'
elif S == 'Rainy':
    answer = 'Sunny'
else:
    answer = '入力間違い【Sunny】【Cloudy】【Rainy】を入力'

print(answer)