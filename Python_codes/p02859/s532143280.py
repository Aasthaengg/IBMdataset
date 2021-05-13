if __name__ == "__main__":
    r = int(input())

    # 半径１の面積 = 1 * 1 * pi
    # 半径ｒの面積 = r * r * pi
    # 半径 r の円の面積が半径 1 の円の面積の何倍になるか = (r*r*pi)/(1*1*pi) = r * r

    print(r*r)