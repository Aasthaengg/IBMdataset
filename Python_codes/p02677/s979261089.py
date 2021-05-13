import math
if __name__ == '__main__':
    a, b, h, m = map(int, input().split())
    h_y = a * math.sin(math.pi* (0.5+(-2)*(h*3600+m*60)/43200))
    h_x = a * math.cos(math.pi* (0.5+(-2)*(h*3600+m*60)/43200))
    m_y = b * math.sin(math.pi* (0.5+(-2)*m/60))
    m_x = b * math.cos(math.pi* (0.5+(-2)*m/60))
    print(math.sqrt((h_y-m_y)**2 + (h_x-m_x)**2))