a_list = list(map(int, input().split()))

ans = "Impossible"

if sum(a_list) % 3 == 0 \
	or a_list[0] % 3 == 0 \
  	or a_list[1] % 3 == 0:
      ans = "Possible"
      
print(ans)