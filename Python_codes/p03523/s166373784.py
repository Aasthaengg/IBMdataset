S = list(input())
ans = 'AKIHABARA'

while len(S) <= len(ans):
	S.append('') # IndexOut対策に空文字列を追加

isCorrect = True

i = 0
while i<(len(ans)):
	# print(i, S[i], ans[i])
	if S[i] == ans[i]:
		i += 1
		continue

	if ans[i] == 'A':
		if S[i] == '':
			S[i] = 'A'
		else:
			S.insert(i,'A')
		continue

	isCorrect = False
	break

S = [s for s in S if s!=''] # IndexOut対策の空文字列を削除

if isCorrect and len(S)==len(ans):
	print('YES')
else:
	print('NO')