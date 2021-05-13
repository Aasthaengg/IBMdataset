n = int(input())
#文字列を同一か判別するために全てsortして格納する
#インプットした文字列をソートして文字列として格納する
s = [''.join(sorted(input())) for _ in range(n)]
#babacaba >>> aaaabbbcとする
######################
#同一性を判定するのにはハッシュテーブルを活用すると良い
#辞書はハッシュテーブルとして高速なために使用
s_dict = {}
for i in range(n):
	if s[i] in s_dict:
		s_dict[s[i]] += 1
	else:
		s_dict[s[i]] = 1
		#辞書内になくとも自動で追加される
		#>>>{xxx:1 yyy:1 zzz:1}
ans = 0
#辞書内の加算された数字についてnCrで2つの組み合わせを検討する
for j in s_dict.values():
	ans += j*(j-1)//2
	#xxxについて、2以上あれば1組は存在するということで+
print(ans)