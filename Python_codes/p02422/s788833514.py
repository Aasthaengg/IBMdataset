string = str(input())

num = int(input())

for a in range(num):
    order = input()
    if "replace" in order: #strのa文字目からb文字目までをpに置き換える
        order,header,footer,p = order.split()
        header = int(header)
        footer = int(footer)
        
        string = string[:header] + p + string[footer+1:]
        
        
    elif "reverse" in order:#strのa文字目からb文字目までを逆順にする。
        order,header,footer = order.split()
        
        header = int(header)
        footer = int(footer)
        
        reverse = string[header:footer+1]  
        reverse = reverse[::-1]
        string = string[:header] + reverse + string[footer+1:]
        

    elif "print" in order:#strのa文字目からb文字目までを出力する
        order,header,footer = order.split()
        header = int(header)
        footer = int(footer)
        print(string[header:footer+1])
