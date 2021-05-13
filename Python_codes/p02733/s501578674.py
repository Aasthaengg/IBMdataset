import sys
input = sys.stdin.readline

H,W,K = map(int,input().split())
choco = [input() for _ in range(H)]
num =(2**(H-1))

white_count = list()
min_div_count =10**6
for i in range(num):
    bin_str = format(i, 'b')
    zero = str()
    if H != len(bin_str):
        for _ in range(H-len(bin_str)):
            zero += "0"
        bin_str = zero + bin_str
    white_count = [0 for s in bin_str if s == "1"]
    white_count.append(0)
    div_count=len(white_count)-1
    
    for j in range(W):
        block_count = 0
        white_list = [0]*len(white_count)
        #print("j:"+str(j))
        is_over = False
        for k in range(len(bin_str)):
            if bin_str[k] == "1":
                block_count += 1
            
            white_list[block_count] += int(choco[k][j])
            white_count[block_count] += int(choco[k][j])
            if white_count[block_count] > K:
                is_over = True

        if max(white_list)>K:
            break


        if is_over:
            div_count += 1
            white_count = white_list


        #print(white_list)   
        #print(white_count)
        #print("div_count"+str(div_count))
        if div_count >= min_div_count:
            break
    else:
        min_div_count = div_count
print(min_div_count)