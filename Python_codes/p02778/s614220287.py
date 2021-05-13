mod = int(1e9+7)
def add(a, b):
    c = a + b
    if c >= mod:
        c -= mod
    return c

def main():
  	n = len(raw_input())
  	temp = ['x' for _ in range(n)]
  	#print(temp)
  	print(''.join(temp))
    #ans = ''.join(temp)
	#print(ans)
    

main()