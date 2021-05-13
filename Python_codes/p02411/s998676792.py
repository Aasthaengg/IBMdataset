while True:
    中間, 期末, 再試験 = map(int, input().split())
    if 中間 < 0 and 期末 < 0 and 再試験 < 0:
        break
    合計点 = 中間 + 期末

    if 中間 < 0 or 期末 < 0:
        print("F")    
    elif 合計点 >= 80:
        print("A")
    elif 65 <= 合計点 and 合計点 < 80:
        print("B")
    elif 50 <= 合計点 and 合計点 < 65:
        print("C")
    elif 30 <= 合計点 and 合計点 < 50:
        if 再試験 >= 50:
            print("C")
        else:
            print("D")
    else:
        print("F")
