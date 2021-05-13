def main():
    a, b, m = map(int, input().split())
    
    # 冷蔵庫
    f_list = list(map(int, input().split()))
    # 電子レンジ
    m_list = list(map(int, input().split()))
    # 割引券
    t_list = [list(map(int, input().split())) for _ in range(m)]
    # 金額
    p_list = []
    
    
    p_list.append(min(f_list) + min(m_list))
    for t in t_list:
        p_list.append(f_list[t[0]-1] + m_list[t[1]-1] - t[2])
    
    ans = min(p_list)
    print(ans)
    

if __name__ == '__main__':
    main()
