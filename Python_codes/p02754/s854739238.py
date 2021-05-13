N,A,B = map(int,input().split())

number_turn = N //(A + B)
nokori = N % (A + B)

if nokori <= A: #nokoriが全てAの場合
	print((number_turn * A) + nokori)
else: #nokoriがAとBの両方の場合
	print((number_turn * A) + A)
